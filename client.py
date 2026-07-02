from typing import Dict, Any

class PriceMonitorClient:
    def monitor_prices(self, sku: str, internal_cost: float, current_price: float, competitor_prices: list) -> Dict[str, Any]:
        avg_comp = sum(competitor_prices) / len(competitor_prices) if competitor_prices else current_price
        target_price = avg_comp - 0.05
        # Do not price below internal cost + 15% safety margin
        min_allowed = internal_cost * 1.15
        final_price = max(min_allowed, target_price)
        return {
            "monitored_sku": sku,
            "average_competitor_price": round(avg_comp, 2),
            "suggested_new_price": round(final_price, 2),
            "repricing_applied": abs(current_price - final_price) > 0.01
        }

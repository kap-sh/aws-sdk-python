from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from capo_partnercentral_benefits._services.async_partner_central_benefits import (
        AsyncPartnerCentralBenefitsClient,
    )
    from capo_partnercentral_benefits._services.partner_central_benefits import (
        PartnerCentralBenefitsClient,
    )


class BenefitApplication:
    def __init__(self, service: PartnerCentralBenefitsClient) -> None:
        self._service = service


class AsyncBenefitApplication:
    def __init__(self, service: AsyncPartnerCentralBenefitsClient) -> None:
        self._service = service

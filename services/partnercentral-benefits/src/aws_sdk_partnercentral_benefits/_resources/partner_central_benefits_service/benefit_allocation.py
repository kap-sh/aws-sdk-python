from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from aws_sdk_partnercentral_benefits._services.async_partner_central_benefits import (
        AsyncPartnerCentralBenefitsClient,
    )
    from aws_sdk_partnercentral_benefits._services.partner_central_benefits import (
        PartnerCentralBenefitsClient,
    )


class BenefitAllocation:
    def __init__(self, service: PartnerCentralBenefitsClient) -> None:
        self._service = service


class AsyncBenefitAllocation:
    def __init__(self, service: AsyncPartnerCentralBenefitsClient) -> None:
        self._service = service

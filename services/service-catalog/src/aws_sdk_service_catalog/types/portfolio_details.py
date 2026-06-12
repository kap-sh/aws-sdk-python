"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PortfolioDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.portfolio_detail

PortfolioDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.portfolio_detail.PortfolioDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortfolioDetails) -> list:
    import aws_sdk_service_catalog.types.portfolio_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.portfolio_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PortfolioDetails:
    import aws_sdk_service_catalog.types.portfolio_detail

    out: PortfolioDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.portfolio_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out

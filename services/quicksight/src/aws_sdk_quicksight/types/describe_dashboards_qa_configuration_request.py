"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardsQAConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id


class DescribeDashboardsQAConfigurationRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard QA configuration that you want described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardsQAConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDashboardsQAConfigurationRequest:
    out: DescribeDashboardsQAConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

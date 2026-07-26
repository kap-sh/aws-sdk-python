"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDashboardsQAConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id


class DescribeDashboardsQAConfigurationRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the dashboard QA configuration that you want described.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDashboardsQAConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeDashboardsQAConfigurationRequest:
    out: DescribeDashboardsQAConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

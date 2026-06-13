"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeSelfUpgradeConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.namespace


class DescribeSelfUpgradeConfigurationRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the Quick self-upgrade configuration.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The Quick namespace that you want to describe the Quick self-upgrade configuration for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSelfUpgradeConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSelfUpgradeConfigurationRequest:
    out: DescribeSelfUpgradeConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out

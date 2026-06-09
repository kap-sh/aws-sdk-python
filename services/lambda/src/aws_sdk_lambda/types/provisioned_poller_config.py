"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedPollerConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.maximum_number_of_pollers
    import aws_sdk_lambda.types.minimum_number_of_pollers
    import aws_sdk_lambda.types.provisioned_poller_group_name


class ProvisionedPollerConfig(TypedDict):
    minimum_pollers: NotRequired[
        "aws_sdk_lambda.types.minimum_number_of_pollers.MinimumNumberOfPollers"
    ]
    """<p>The minimum number of event pollers this event source can scale down to. For Amazon SQS events source mappings, default is 2, and minimum 2 required. For Amazon MSK and self-managed Apache Kafka event source mappings, default is 1.</p>"""
    maximum_pollers: NotRequired[
        "aws_sdk_lambda.types.maximum_number_of_pollers.MaximumNumberOfPollers"
    ]
    """<p>The maximum number of event pollers this event source can scale up to. For Amazon SQS events source mappings, default is 200, and minimum value allowed is 2. For Amazon MSK and self-managed Apache Kafka event source mappings, default is 200, and minimum value allowed is 1.</p>"""
    poller_group_name: NotRequired[
        "aws_sdk_lambda.types.provisioned_poller_group_name.ProvisionedPollerGroupName"
    ]
    """<p>(Amazon MSK and self-managed Apache Kafka) The name of the provisioned poller group. Use this option to group multiple ESMs within the event source's VPC to share Event Poller Unit (EPU) capacity. You can use this option to optimize Provisioned mode costs for your ESMs. You can group up to 100 ESMs per poller group and aggregate maximum pollers across all ESMs in a group cannot exceed 2000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedPollerConfig) -> dict:
    out: dict = {}
    if "minimum_pollers" in value:
        out["MinimumPollers"] = value["minimum_pollers"]
    if "maximum_pollers" in value:
        out["MaximumPollers"] = value["maximum_pollers"]
    if "poller_group_name" in value:
        out["PollerGroupName"] = value["poller_group_name"]
    return out


def deserialize_json(data: dict) -> ProvisionedPollerConfig:
    out: ProvisionedPollerConfig = {}  # type: ignore[typeddict-item]
    if "MinimumPollers" in data:
        out["minimum_pollers"] = data["MinimumPollers"]
    if "MaximumPollers" in data:
        out["maximum_pollers"] = data["MaximumPollers"]
    if "PollerGroupName" in data:
        out["poller_group_name"] = data["PollerGroupName"]
    return out

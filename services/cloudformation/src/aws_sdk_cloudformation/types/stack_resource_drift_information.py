"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackResourceDriftInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.stack_resource_drift_status
    import aws_sdk_cloudformation.types.timestamp


class StackResourceDriftInformation(TypedDict):
    stack_resource_drift_status: NotRequired[
        "aws_sdk_cloudformation.types.stack_resource_drift_status.StackResourceDriftStatus"
    ]
    r"""<p>Status of the resource's actual configuration compared to its expected configuration</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected configuration in that it has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: The resource differs from its expected configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation has not checked if the resource differs from its expected configuration.</p> <p>Any resources that do not currently support drift detection have a status of <code>NOT_CHECKED</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html\">Resource type support for imports and drift detection</a>.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected configuration.</p> </li> </ul>"""
    last_check_timestamp: NotRequired[
        "aws_sdk_cloudformation.types.timestamp.Timestamp"
    ]
    """<p>When CloudFormation last checked if the resource had drifted from its expected configuration.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StackResourceDriftInformation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "stack_resource_drift_status" in value:
        import aws_sdk_cloudformation.types.stack_resource_drift_status

        aws_sdk_cloudformation.types.stack_resource_drift_status.serialize_query(
            value["stack_resource_drift_status"],
            pairs,
            f"{prefix}.StackResourceDriftStatus",
        )
    if "last_check_timestamp" in value:
        import aws_sdk_cloudformation.types.timestamp

        aws_sdk_cloudformation.types.timestamp.serialize_query(
            value["last_check_timestamp"], pairs, f"{prefix}.LastCheckTimestamp"
        )


def deserialize_query(el: Element) -> StackResourceDriftInformation:
    out: StackResourceDriftInformation = {}  # type: ignore[typeddict-item]
    child_stack_resource_drift_status = el.find("StackResourceDriftStatus")
    if child_stack_resource_drift_status is not None:
        import aws_sdk_cloudformation.types.stack_resource_drift_status

        out["stack_resource_drift_status"] = (
            aws_sdk_cloudformation.types.stack_resource_drift_status.deserialize_query(
                child_stack_resource_drift_status
            )
        )
    child_last_check_timestamp = el.find("LastCheckTimestamp")
    if child_last_check_timestamp is not None:
        import aws_sdk_cloudformation.types.timestamp

        out["last_check_timestamp"] = (
            aws_sdk_cloudformation.types.timestamp.deserialize_query(
                child_last_check_timestamp
            )
        )
    return out

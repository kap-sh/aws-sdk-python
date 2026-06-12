"""Generated from Smithy shape ``com.amazonaws.cloudformation#LoggingConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.log_group_name
    import aws_sdk_cloudformation.types.role_arn2


class LoggingConfig(TypedDict):
    log_role_arn: NotRequired["aws_sdk_cloudformation.types.role_arn2.RoleARN2"]
    """<p>The Amazon Resource Name (ARN) of the role that CloudFormation should assume when sending log entries to CloudWatch Logs.</p>"""
    log_group_name: NotRequired[
        "aws_sdk_cloudformation.types.log_group_name.LogGroupName"
    ]
    """<p>The Amazon CloudWatch Logs group to which CloudFormation sends error logging information when invoking the extension's handlers.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LoggingConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "log_role_arn" in value:
        pairs.append((f"{prefix}.LogRoleArn", str(value["log_role_arn"])))
    if "log_group_name" in value:
        pairs.append((f"{prefix}.LogGroupName", str(value["log_group_name"])))


def deserialize_query(el: Element) -> LoggingConfig:
    out: LoggingConfig = {}  # type: ignore[typeddict-item]
    child_log_role_arn = el.find("LogRoleArn")
    if child_log_role_arn is not None:
        out["log_role_arn"] = str(child_log_role_arn.text or "")
    child_log_group_name = el.find("LogGroupName")
    if child_log_group_name is not None:
        out["log_group_name"] = str(child_log_group_name.text or "")
    return out

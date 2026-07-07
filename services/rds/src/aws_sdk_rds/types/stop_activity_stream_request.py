"""Generated from Smithy shape ``com.amazonaws.rds#StopActivityStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.boolean_optional
    import aws_sdk_rds.types.string


class StopActivityStreamRequest(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the DB cluster for the database activity stream. For example, <code>arn:aws:rds:us-east-1:12345667890:cluster:das-cluster</code>.</p>"""
    apply_immediately: NotRequired["aws_sdk_rds.types.boolean_optional.BooleanOptional"]
    """<p>Specifies whether or not the database activity stream is to stop as soon as possible, regardless of the maintenance window for the database.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopActivityStreamRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_arn" in value:
        pairs.append((f"{prefix}.ResourceArn", str(value["resource_arn"])))
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> StopActivityStreamRequest:
    out: StopActivityStreamRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out

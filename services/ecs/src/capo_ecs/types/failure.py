"""Generated from Smithy shape ``com.amazonaws.ecs#Failure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class Failure(TypedDict, closed=True):
    arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the failed resource.</p>"""
    reason: NotRequired["capo_ecs.types.string.String"]
    """<p>The reason for the failure.</p>"""
    detail: NotRequired["capo_ecs.types.string.String"]
    """<p>The details of the failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Failure) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "reason" in value:
        out["reason"] = value["reason"]
    if "detail" in value:
        out["detail"] = value["detail"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Failure:
    out: Failure = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("detail") is not None:
        out["detail"] = data["detail"]
    return out

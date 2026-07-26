"""Generated from Smithy shape ``com.amazonaws.ecs#CreatedAt``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.timestamp


class CreatedAt(TypedDict, closed=True):
    before: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>Include service deployments in the result that were created before this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    after: NotRequired["capo_ecs.types.timestamp.Timestamp"]
    """<p>Include service deployments in the result that were created after this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreatedAt) -> dict:
    out: dict = {}
    if "before" in value:
        import capo_ecs.types.timestamp

        out["before"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(value["before"])
    if "after" in value:
        import capo_ecs.types.timestamp

        out["after"] = capo_ecs.types.timestamp.serialize_aws_json_1_1(value["after"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreatedAt:
    out: CreatedAt = {}  # type: ignore[typeddict-item]
    if "before" in data:
        import capo_ecs.types.timestamp

        out["before"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(
            data["before"]
        )
    if "after" in data:
        import capo_ecs.types.timestamp

        out["after"] = capo_ecs.types.timestamp.deserialize_aws_json_1_1(data["after"])
    return out

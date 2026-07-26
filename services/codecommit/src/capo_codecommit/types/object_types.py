"""Generated from Smithy shape ``com.amazonaws.codecommit#ObjectTypes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_type_enum


class ObjectTypes(TypedDict, closed=True):
    source: NotRequired["capo_codecommit.types.object_type_enum.ObjectTypeEnum"]
    """<p>The type of the object in the source branch.</p>"""
    destination: NotRequired["capo_codecommit.types.object_type_enum.ObjectTypeEnum"]
    """<p>The type of the object in the destination branch.</p>"""
    base: NotRequired["capo_codecommit.types.object_type_enum.ObjectTypeEnum"]
    """<p>The type of the object in the base commit of the merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectTypes) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_codecommit.types.object_type_enum

        out["source"] = capo_codecommit.types.object_type_enum.serialize_aws_json_1_1(
            value["source"]
        )
    if "destination" in value:
        import capo_codecommit.types.object_type_enum

        out["destination"] = (
            capo_codecommit.types.object_type_enum.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "base" in value:
        import capo_codecommit.types.object_type_enum

        out["base"] = capo_codecommit.types.object_type_enum.serialize_aws_json_1_1(
            value["base"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ObjectTypes:
    out: ObjectTypes = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import capo_codecommit.types.object_type_enum

        out["source"] = capo_codecommit.types.object_type_enum.deserialize_aws_json_1_1(
            data["source"]
        )
    if "destination" in data:
        import capo_codecommit.types.object_type_enum

        out["destination"] = (
            capo_codecommit.types.object_type_enum.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    if "base" in data:
        import capo_codecommit.types.object_type_enum

        out["base"] = capo_codecommit.types.object_type_enum.deserialize_aws_json_1_1(
            data["base"]
        )
    return out

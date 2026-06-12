"""Generated from Smithy shape ``com.amazonaws.codecommit#ObjectTypes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_type_enum


class ObjectTypes(TypedDict):
    source: NotRequired["aws_sdk_codecommit.types.object_type_enum.ObjectTypeEnum"]
    """<p>The type of the object in the source branch.</p>"""
    destination: NotRequired["aws_sdk_codecommit.types.object_type_enum.ObjectTypeEnum"]
    """<p>The type of the object in the destination branch.</p>"""
    base: NotRequired["aws_sdk_codecommit.types.object_type_enum.ObjectTypeEnum"]
    """<p>The type of the object in the base commit of the merge.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectTypes) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_codecommit.types.object_type_enum

        out["source"] = (
            aws_sdk_codecommit.types.object_type_enum.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "destination" in value:
        import aws_sdk_codecommit.types.object_type_enum

        out["destination"] = (
            aws_sdk_codecommit.types.object_type_enum.serialize_aws_json_1_1(
                value["destination"]
            )
        )
    if "base" in value:
        import aws_sdk_codecommit.types.object_type_enum

        out["base"] = aws_sdk_codecommit.types.object_type_enum.serialize_aws_json_1_1(
            value["base"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ObjectTypes:
    out: ObjectTypes = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_codecommit.types.object_type_enum

        out["source"] = (
            aws_sdk_codecommit.types.object_type_enum.deserialize_aws_json_1_1(
                data["source"]
            )
        )
    if "destination" in data:
        import aws_sdk_codecommit.types.object_type_enum

        out["destination"] = (
            aws_sdk_codecommit.types.object_type_enum.deserialize_aws_json_1_1(
                data["destination"]
            )
        )
    if "base" in data:
        import aws_sdk_codecommit.types.object_type_enum

        out["base"] = (
            aws_sdk_codecommit.types.object_type_enum.deserialize_aws_json_1_1(
                data["base"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.codepipeline#BlockerDeclaration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.blocker_name
    import aws_sdk_codepipeline.types.blocker_type


class BlockerDeclaration(TypedDict):
    name: "aws_sdk_codepipeline.types.blocker_name.BlockerName"
    """<p>Reserved for future use.</p>"""
    type: "aws_sdk_codepipeline.types.blocker_type.BlockerType"
    """<p>Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlockerDeclaration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_codepipeline.types.blocker_type

    out["type"] = aws_sdk_codepipeline.types.blocker_type.serialize_aws_json_1_1(
        value["type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BlockerDeclaration:
    out: BlockerDeclaration = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("BlockerDeclaration.name required")
    if "type" in data:
        import aws_sdk_codepipeline.types.blocker_type

        out["type"] = aws_sdk_codepipeline.types.blocker_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("BlockerDeclaration.type required")
    return out

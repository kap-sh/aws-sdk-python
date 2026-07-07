"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTagsForResourceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.tag_map_output


class ListTagsForResourceOutput(TypedDict, closed=True):
    tags: "aws_sdk_observabilityadmin.types.tag_map_output.TagMapOutput"
    """<p> The list of tags associated with the telemetry rule resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceOutput) -> dict:
    out: dict = {}
    import aws_sdk_observabilityadmin.types.tag_map_output

    out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_output.serialize_json(
        value["tags"]
    )
    return out


def deserialize_json(data: dict) -> ListTagsForResourceOutput:
    out: ListTagsForResourceOutput = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_output.deserialize_json(
            data["Tags"]
        )
    else:
        raise DeserializationError("ListTagsForResourceOutput.tags required")
    return out

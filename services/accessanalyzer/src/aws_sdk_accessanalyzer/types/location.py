"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#Location``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.path_element_list
    import aws_sdk_accessanalyzer.types.span


class Location(TypedDict):
    path: "aws_sdk_accessanalyzer.types.path_element_list.PathElementList"
    """<p>A path in a policy, represented as a sequence of path elements.</p>"""
    span: "aws_sdk_accessanalyzer.types.span.Span"
    """<p>A span in a policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Location) -> dict:
    out: dict = {}
    import aws_sdk_accessanalyzer.types.path_element_list

    out["path"] = aws_sdk_accessanalyzer.types.path_element_list.serialize_json(
        value["path"]
    )
    import aws_sdk_accessanalyzer.types.span

    out["span"] = aws_sdk_accessanalyzer.types.span.serialize_json(value["span"])
    return out


def deserialize_json(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if "path" in data:
        import aws_sdk_accessanalyzer.types.path_element_list

        out["path"] = aws_sdk_accessanalyzer.types.path_element_list.deserialize_json(
            data["path"]
        )
    else:
        raise DeserializationError("Location.path required")
    if "span" in data:
        import aws_sdk_accessanalyzer.types.span

        out["span"] = aws_sdk_accessanalyzer.types.span.deserialize_json(data["span"])
    else:
        raise DeserializationError("Location.span required")
    return out

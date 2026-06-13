"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchExpression``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.filter_list


class SearchExpression(TypedDict):
    filters: "aws_sdk_qconnect.types.filter_list.FilterList"
    """<p>The search expression filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchExpression) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.filter_list

    out["filters"] = aws_sdk_qconnect.types.filter_list.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> SearchExpression:
    out: SearchExpression = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_qconnect.types.filter_list

        out["filters"] = aws_sdk_qconnect.types.filter_list.deserialize_json(
            data["filters"]
        )
    else:
        raise DeserializationError("SearchExpression.filters required")
    return out

"""Generated from Smithy shape ``com.amazonaws.dataexchange#TableLFTagPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_lf_tags


class TableLFTagPolicy(TypedDict, closed=True):
    expression: "aws_sdk_dataexchange.types.list_of_lf_tags.ListOfLFTags"
    """<p>A list of LF-tag conditions that apply to table resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableLFTagPolicy) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_lf_tags

    out["Expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> TableLFTagPolicy:
    out: TableLFTagPolicy = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        import aws_sdk_dataexchange.types.list_of_lf_tags

        out["expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError("TableLFTagPolicy.expression required")
    return out

"""Generated from Smithy shape ``com.amazonaws.dataexchange#DatabaseLFTagPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.list_of_lf_tags


class DatabaseLFTagPolicy(TypedDict, closed=True):
    expression: "aws_sdk_dataexchange.types.list_of_lf_tags.ListOfLFTags"
    """<p>A list of LF-tag conditions that apply to database resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatabaseLFTagPolicy) -> dict:
    out: dict = {}
    import aws_sdk_dataexchange.types.list_of_lf_tags

    out["Expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.serialize_json(
        value["expression"]
    )
    return out


def deserialize_json(data: dict) -> DatabaseLFTagPolicy:
    out: DatabaseLFTagPolicy = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        import aws_sdk_dataexchange.types.list_of_lf_tags

        out["expression"] = aws_sdk_dataexchange.types.list_of_lf_tags.deserialize_json(
            data["Expression"]
        )
    else:
        raise DeserializationError("DatabaseLFTagPolicy.expression required")
    return out

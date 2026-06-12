"""Generated from Smithy shape ``com.amazonaws.athena#Row``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.datum_list


class Row(TypedDict):
    data: NotRequired["aws_sdk_athena.types.datum_list.datumList"]
    """<p>The data that populates a row in a query result table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Row) -> dict:
    out: dict = {}
    if "data" in value:
        import aws_sdk_athena.types.datum_list

        out["Data"] = aws_sdk_athena.types.datum_list.serialize_aws_json_1_1(
            value["data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if "Data" in data:
        import aws_sdk_athena.types.datum_list

        out["data"] = aws_sdk_athena.types.datum_list.deserialize_aws_json_1_1(
            data["Data"]
        )
    return out

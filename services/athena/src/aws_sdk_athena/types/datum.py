"""Generated from Smithy shape ``com.amazonaws.athena#Datum``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.datum_string


class Datum(TypedDict, closed=True):
    var_char_value: NotRequired["aws_sdk_athena.types.datum_string.datumString"]
    """<p>The value of the datum.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Datum) -> dict:
    out: dict = {}
    if "var_char_value" in value:
        out["VarCharValue"] = value["var_char_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Datum:
    out: Datum = {}  # type: ignore[typeddict-item]
    if "VarCharValue" in data:
        out["var_char_value"] = data["VarCharValue"]
    return out

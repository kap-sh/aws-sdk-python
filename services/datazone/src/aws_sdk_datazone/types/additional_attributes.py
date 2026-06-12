"""Generated from Smithy shape ``com.amazonaws.datazone#AdditionalAttributes``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_datazone.types.form_name_list

class AdditionalAttributes(TypedDict):
    form_names: NotRequired["aws_sdk_datazone.types.form_name_list.FormNameList"]
    """<p>Names of forms on the query entity that can be requested in the response.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AdditionalAttributes) -> dict:
    out: dict = {}
    if "form_names" in value:
        import aws_sdk_datazone.types.form_name_list
        out["formNames"] = aws_sdk_datazone.types.form_name_list.serialize_json(value["form_names"])
    return out


def deserialize_json(data: dict) -> AdditionalAttributes:
    out: AdditionalAttributes = {}  # type: ignore[typeddict-item]
    if "formNames" in data:
        import aws_sdk_datazone.types.form_name_list
        out["form_names"] = aws_sdk_datazone.types.form_name_list.deserialize_json(data["formNames"])
    return out
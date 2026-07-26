"""Generated from Smithy shape ``com.amazonaws.emr#SupportedProductConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string_list
    import capo_emr.types.xml_string_max_len256


class SupportedProductConfig(TypedDict, closed=True):
    name: NotRequired["capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the product configuration.</p>"""
    args: NotRequired["capo_emr.types.xml_string_list.XmlStringList"]
    """<p>The list of user-supplied arguments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedProductConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "args" in value:
        import capo_emr.types.xml_string_list

        out["Args"] = capo_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedProductConfig:
    out: SupportedProductConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Args" in data:
        import capo_emr.types.xml_string_list

        out["args"] = capo_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out

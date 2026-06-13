"""Generated from Smithy shape ``com.amazonaws.emr#SupportedProductConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_list
    import aws_sdk_emr.types.xml_string_max_len256


class SupportedProductConfig(TypedDict):
    name: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The name of the product configuration.</p>"""
    args: NotRequired["aws_sdk_emr.types.xml_string_list.XmlStringList"]
    """<p>The list of user-supplied arguments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedProductConfig) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "args" in value:
        import aws_sdk_emr.types.xml_string_list

        out["Args"] = aws_sdk_emr.types.xml_string_list.serialize_aws_json_1_1(
            value["args"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SupportedProductConfig:
    out: SupportedProductConfig = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Args" in data:
        import aws_sdk_emr.types.xml_string_list

        out["args"] = aws_sdk_emr.types.xml_string_list.deserialize_aws_json_1_1(
            data["Args"]
        )
    return out

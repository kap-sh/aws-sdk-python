"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppUnits``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_transfer.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_transfer.types.web_app_unit_count


class _WebAppUnits_Provisioned(TypedDict, closed=True):
    Provisioned: "aws_sdk_transfer.types.web_app_unit_count.WebAppUnitCount"


WebAppUnits: TypeAlias = _WebAppUnits_Provisioned


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppUnits) -> dict:
    if "Provisioned" in value:
        return {"Provisioned": value["Provisioned"]}
    else:
        raise SerializationError("WebAppUnits: no variant present")


def deserialize_aws_json_1_1(data: dict) -> WebAppUnits:
    if "Provisioned" in data:
        return {"Provisioned": data["Provisioned"]}
    else:
        raise DeserializationError("WebAppUnits: no recognized variant key")

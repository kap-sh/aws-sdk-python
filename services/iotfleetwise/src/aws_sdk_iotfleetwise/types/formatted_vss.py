"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#FormattedVss``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, SerializationError


class _FormattedVss_vssJson(TypedDict, closed=True):
    vssJson: "str"


FormattedVss: TypeAlias = _FormattedVss_vssJson


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FormattedVss) -> dict:
    if "vssJson" in value:
        return {"vssJson": value["vssJson"]}
    else:
        raise SerializationError("FormattedVss: no variant present")


def deserialize_aws_json_1_0(data: dict) -> FormattedVss:
    if "vssJson" in data:
        return {"vssJson": data["vssJson"]}
    else:
        raise DeserializationError("FormattedVss: no recognized variant key")

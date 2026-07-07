"""Generated from Smithy shape ``com.amazonaws.braket#SearchDevicesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.string256_list


class SearchDevicesFilter(TypedDict, closed=True):
    name: "str"
    """<p>The name of the device parameter to filter based on. Only <code>deviceArn</code> filter name is currently supported.</p>"""
    values: "aws_sdk_braket.types.string256_list.String256List"
    """<p>The values used to filter devices based on the filter name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDevicesFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_braket.types.string256_list

    out["values"] = aws_sdk_braket.types.string256_list.serialize_json(value["values"])
    return out


def deserialize_json(data: dict) -> SearchDevicesFilter:
    out: SearchDevicesFilter = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SearchDevicesFilter.name required")
    if "values" in data:
        import aws_sdk_braket.types.string256_list

        out["values"] = aws_sdk_braket.types.string256_list.deserialize_json(
            data["values"]
        )
    else:
        raise DeserializationError("SearchDevicesFilter.values required")
    return out

"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_quicksetup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_quicksetup.types.filter_values


class Filter(TypedDict, closed=True):
    key: "str"
    """<p>The key for the filter.</p>"""
    values: "aws_sdk_ssm_quicksetup.types.filter_values.FilterValues"
    """<p>The values for the filter keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Filter) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_ssm_quicksetup.types.filter_values

    out["Values"] = aws_sdk_ssm_quicksetup.types.filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("Filter.key required")
    if "Values" in data:
        import aws_sdk_ssm_quicksetup.types.filter_values

        out["values"] = aws_sdk_ssm_quicksetup.types.filter_values.deserialize_json(
            data["Values"]
        )
    else:
        raise DeserializationError("Filter.values required")
    return out

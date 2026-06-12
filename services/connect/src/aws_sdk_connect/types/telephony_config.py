"""Generated from Smithy shape ``com.amazonaws.connect#TelephonyConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.distribution_list


class TelephonyConfig(TypedDict):
    distributions: "aws_sdk_connect.types.distribution_list.DistributionList"
    """<p>Information about traffic distributions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyConfig) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.distribution_list

    out["Distributions"] = aws_sdk_connect.types.distribution_list.serialize_json(
        value["distributions"]
    )
    return out


def deserialize_json(data: dict) -> TelephonyConfig:
    out: TelephonyConfig = {}  # type: ignore[typeddict-item]
    if "Distributions" in data:
        import aws_sdk_connect.types.distribution_list

        out["distributions"] = aws_sdk_connect.types.distribution_list.deserialize_json(
            data["Distributions"]
        )
    else:
        raise DeserializationError("TelephonyConfig.distributions required")
    return out

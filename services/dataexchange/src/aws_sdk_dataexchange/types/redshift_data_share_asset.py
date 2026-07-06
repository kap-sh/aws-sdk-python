"""Generated from Smithy shape ``com.amazonaws.dataexchange#RedshiftDataShareAsset``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.__string


class RedshiftDataShareAsset(TypedDict, closed=True):
    arn: "aws_sdk_dataexchange.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the datashare asset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftDataShareAsset) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> RedshiftDataShareAsset:
    out: RedshiftDataShareAsset = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("RedshiftDataShareAsset.arn required")
    return out

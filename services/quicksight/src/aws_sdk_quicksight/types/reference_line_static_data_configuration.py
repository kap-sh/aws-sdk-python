"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineStaticDataConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sensitive_double


class ReferenceLineStaticDataConfiguration(TypedDict, closed=True):
    value: "aws_sdk_quicksight.types.sensitive_double.SensitiveDouble"
    """<p>The double input of the static data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineStaticDataConfiguration) -> dict:
    out: dict = {}
    out["Value"] = value.get("value", 0)
    return out


def deserialize_json(data: dict) -> ReferenceLineStaticDataConfiguration:
    out: ReferenceLineStaticDataConfiguration = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    return out

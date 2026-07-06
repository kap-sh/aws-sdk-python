"""Generated from Smithy shape ``com.amazonaws.swf#DeprecateDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_swf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_swf.types.domain_name


class DeprecateDomainInput(TypedDict, closed=True):
    name: "aws_sdk_swf.types.domain_name.DomainName"
    """<p>The name of the domain to deprecate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeprecateDomainInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeprecateDomainInput:
    out: DeprecateDomainInput = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DeprecateDomainInput.name required")
    return out

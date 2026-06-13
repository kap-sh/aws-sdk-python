"""Generated from Smithy shape ``com.amazonaws.controlcatalog#DomainResourceFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.domain_arn


class DomainResourceFilter(TypedDict):
    arn: NotRequired["aws_sdk_controlcatalog.types.domain_arn.DomainArn"]
    """<p>The Amazon Resource Name (ARN) of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainResourceFilter) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> DomainResourceFilter:
    out: DomainResourceFilter = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out

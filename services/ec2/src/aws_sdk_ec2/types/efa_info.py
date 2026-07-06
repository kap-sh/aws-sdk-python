"""Generated from Smithy shape ``com.amazonaws.ec2#EfaInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.maximum_efa_interfaces


class EfaInfo(TypedDict, closed=True):
    maximum_efa_interfaces: NotRequired[
        "aws_sdk_ec2.types.maximum_efa_interfaces.MaximumEfaInterfaces"
    ]
    """<p>The maximum number of Elastic Fabric Adapters for the instance type.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EfaInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "maximum_efa_interfaces" in value:
        pairs.append(
            (f"{prefix}.MaximumEfaInterfaces", str(value["maximum_efa_interfaces"]))
        )


def deserialize_ec2_query(el: Element) -> EfaInfo:
    out: EfaInfo = {}  # type: ignore[typeddict-item]
    child_maximum_efa_interfaces = el.find("MaximumEfaInterfaces")
    if child_maximum_efa_interfaces is not None:
        out["maximum_efa_interfaces"] = int(child_maximum_efa_interfaces.text or "")
    return out

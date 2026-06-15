"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTrunkInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trunk_interface_association


class AssociateTrunkInterfaceResult(TypedDict):
    interface_association: NotRequired[
        "aws_sdk_ec2.types.trunk_interface_association.TrunkInterfaceAssociation"
    ]
    """<p>Information about the association between the trunk network interface and branch network interface.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    r"""<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateTrunkInterfaceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "interface_association" in value:
        import aws_sdk_ec2.types.trunk_interface_association

        aws_sdk_ec2.types.trunk_interface_association.serialize_ec2_query(
            value["interface_association"], pairs, f"{prefix}.InterfaceAssociation"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> AssociateTrunkInterfaceResult:
    out: AssociateTrunkInterfaceResult = {}  # type: ignore[typeddict-item]
    child_interface_association = el.find("InterfaceAssociation")
    if child_interface_association is not None:
        import aws_sdk_ec2.types.trunk_interface_association

        out["interface_association"] = (
            aws_sdk_ec2.types.trunk_interface_association.deserialize_ec2_query(
                child_interface_association
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out

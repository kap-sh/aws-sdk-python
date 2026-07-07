"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVerifiedAccessInstanceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.verified_access_instance


class DeleteVerifiedAccessInstanceResult(TypedDict, closed=True):
    verified_access_instance: NotRequired[
        "aws_sdk_ec2.types.verified_access_instance.VerifiedAccessInstance"
    ]
    """<p>Details about the Verified Access instance.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVerifiedAccessInstanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "verified_access_instance" in value:
        import aws_sdk_ec2.types.verified_access_instance

        aws_sdk_ec2.types.verified_access_instance.serialize_ec2_query(
            value["verified_access_instance"], pairs, f"{prefix}.VerifiedAccessInstance"
        )


def deserialize_ec2_query(el: Element) -> DeleteVerifiedAccessInstanceResult:
    out: DeleteVerifiedAccessInstanceResult = {}  # type: ignore[typeddict-item]
    child_verified_access_instance = el.find("VerifiedAccessInstance")
    if child_verified_access_instance is not None:
        import aws_sdk_ec2.types.verified_access_instance

        out["verified_access_instance"] = (
            aws_sdk_ec2.types.verified_access_instance.deserialize_ec2_query(
                child_verified_access_instance
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProviderCondensed``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.device_trust_provider_type
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.trust_provider_type
    import aws_sdk_ec2.types.user_trust_provider_type


class VerifiedAccessTrustProviderCondensed(TypedDict):
    verified_access_trust_provider_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the trust provider.</p>"""
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The description of trust provider.</p>"""
    trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.trust_provider_type.TrustProviderType"
    ]
    """<p>The type of trust provider (user- or device-based).</p>"""
    user_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The type of user-based trust provider.</p>"""
    device_trust_provider_type: NotRequired[
        "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
    ]
    """<p>The type of device-based trust provider.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessTrustProviderCondensed,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "verified_access_trust_provider_id" in value:
        pairs.append(
            (
                f"{prefix}.VerifiedAccessTrustProviderId",
                str(value["verified_access_trust_provider_id"]),
            )
        )
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "trust_provider_type" in value:
        import aws_sdk_ec2.types.trust_provider_type

        aws_sdk_ec2.types.trust_provider_type.serialize_ec2_query(
            value["trust_provider_type"], pairs, f"{prefix}.TrustProviderType"
        )
    if "user_trust_provider_type" in value:
        import aws_sdk_ec2.types.user_trust_provider_type

        aws_sdk_ec2.types.user_trust_provider_type.serialize_ec2_query(
            value["user_trust_provider_type"], pairs, f"{prefix}.UserTrustProviderType"
        )
    if "device_trust_provider_type" in value:
        import aws_sdk_ec2.types.device_trust_provider_type

        aws_sdk_ec2.types.device_trust_provider_type.serialize_ec2_query(
            value["device_trust_provider_type"],
            pairs,
            f"{prefix}.DeviceTrustProviderType",
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessTrustProviderCondensed:
    out: VerifiedAccessTrustProviderCondensed = {}  # type: ignore[typeddict-item]
    child_verified_access_trust_provider_id = el.find("VerifiedAccessTrustProviderId")
    if child_verified_access_trust_provider_id is not None:
        out["verified_access_trust_provider_id"] = str(
            child_verified_access_trust_provider_id.text or ""
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_trust_provider_type = el.find("TrustProviderType")
    if child_trust_provider_type is not None:
        import aws_sdk_ec2.types.trust_provider_type

        out["trust_provider_type"] = (
            aws_sdk_ec2.types.trust_provider_type.deserialize_ec2_query(
                child_trust_provider_type
            )
        )
    child_user_trust_provider_type = el.find("UserTrustProviderType")
    if child_user_trust_provider_type is not None:
        import aws_sdk_ec2.types.user_trust_provider_type

        out["user_trust_provider_type"] = (
            aws_sdk_ec2.types.user_trust_provider_type.deserialize_ec2_query(
                child_user_trust_provider_type
            )
        )
    child_device_trust_provider_type = el.find("DeviceTrustProviderType")
    if child_device_trust_provider_type is not None:
        import aws_sdk_ec2.types.device_trust_provider_type

        out["device_trust_provider_type"] = (
            aws_sdk_ec2.types.device_trust_provider_type.deserialize_ec2_query(
                child_device_trust_provider_type
            )
        )
    return out

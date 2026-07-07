"""Generated from Smithy shape ``com.amazonaws.ec2#DeviceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeviceOptions(TypedDict, closed=True):
    tenant_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the tenant application with the device-identity provider.</p>"""
    public_signing_key_url: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The URL Amazon Web Services Verified Access will use to verify the authenticity of the device tokens. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeviceOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "tenant_id" in value:
        pairs.append((f"{prefix}.TenantId", str(value["tenant_id"])))
    if "public_signing_key_url" in value:
        pairs.append(
            (f"{prefix}.PublicSigningKeyUrl", str(value["public_signing_key_url"]))
        )


def deserialize_ec2_query(el: Element) -> DeviceOptions:
    out: DeviceOptions = {}  # type: ignore[typeddict-item]
    child_tenant_id = el.find("TenantId")
    if child_tenant_id is not None:
        out["tenant_id"] = str(child_tenant_id.text or "")
    child_public_signing_key_url = el.find("PublicSigningKeyUrl")
    if child_public_signing_key_url is not None:
        out["public_signing_key_url"] = str(child_public_signing_key_url.text or "")
    return out

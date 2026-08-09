"""Generated from Smithy shape ``com.amazonaws.ec2#IpamExternalResourceVerificationToken``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_external_resource_verification_token_id
    import capo_ec2.types.ipam_external_resource_verification_token_state
    import capo_ec2.types.ipam_id
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.resource_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.token_state


class IpamExternalResourceVerificationToken(TypedDict, closed=True):
    ipam_external_resource_verification_token_id: NotRequired[
        "capo_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>The ID of the token.</p>"""
    ipam_external_resource_verification_token_arn: NotRequired[
        "capo_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>Token ARN.</p>"""
    ipam_id: NotRequired["capo_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM that created the token.</p>"""
    ipam_arn: NotRequired["capo_ec2.types.resource_arn.ResourceArn"]
    """<p>ARN of the IPAM that created the token.</p>"""
    ipam_region: NotRequired["capo_ec2.types.string.String"]
    """<p>Region of the IPAM that created the token.</p>"""
    token_value: NotRequired["capo_ec2.types.string.String"]
    """<p>Token value.</p>"""
    token_name: NotRequired["capo_ec2.types.string.String"]
    """<p>Token name.</p>"""
    not_after: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>Token expiration.</p>"""
    status: NotRequired["capo_ec2.types.token_state.TokenState"]
    """<p>Token status.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Token tags.</p>"""
    state: NotRequired[
        "capo_ec2.types.ipam_external_resource_verification_token_state.IpamExternalResourceVerificationTokenState"
    ]
    """<p>Token state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamExternalResourceVerificationToken,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipam_external_resource_verification_token_id" in value:
        pairs.append(
            (
                f"{key_prefix}IpamExternalResourceVerificationTokenId",
                str(value["ipam_external_resource_verification_token_id"]),
            )
        )
    if "ipam_external_resource_verification_token_arn" in value:
        pairs.append(
            (
                f"{key_prefix}IpamExternalResourceVerificationTokenArn",
                str(value["ipam_external_resource_verification_token_arn"]),
            )
        )
    if "ipam_id" in value:
        pairs.append((f"{key_prefix}IpamId", str(value["ipam_id"])))
    if "ipam_arn" in value:
        pairs.append((f"{key_prefix}IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{key_prefix}IpamRegion", str(value["ipam_region"])))
    if "token_value" in value:
        pairs.append((f"{key_prefix}TokenValue", str(value["token_value"])))
    if "token_name" in value:
        pairs.append((f"{key_prefix}TokenName", str(value["token_name"])))
    if "not_after" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["not_after"], pairs, f"{key_prefix}NotAfter"
        )
    if "status" in value:
        import capo_ec2.types.token_state

        capo_ec2.types.token_state.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "state" in value:
        import capo_ec2.types.ipam_external_resource_verification_token_state

        capo_ec2.types.ipam_external_resource_verification_token_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )


def deserialize_ec2_query(el: Element) -> IpamExternalResourceVerificationToken:
    out: IpamExternalResourceVerificationToken = {}  # type: ignore[typeddict-item]
    child_ipam_external_resource_verification_token_id = el.find(
        "ipamExternalResourceVerificationTokenId"
    )
    if child_ipam_external_resource_verification_token_id is not None:
        out["ipam_external_resource_verification_token_id"] = str(
            child_ipam_external_resource_verification_token_id.text or ""
        )
    child_ipam_external_resource_verification_token_arn = el.find(
        "ipamExternalResourceVerificationTokenArn"
    )
    if child_ipam_external_resource_verification_token_arn is not None:
        out["ipam_external_resource_verification_token_arn"] = str(
            child_ipam_external_resource_verification_token_arn.text or ""
        )
    child_ipam_id = el.find("ipamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_arn = el.find("ipamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("ipamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_token_value = el.find("tokenValue")
    if child_token_value is not None:
        out["token_value"] = str(child_token_value.text or "")
    child_token_name = el.find("tokenName")
    if child_token_name is not None:
        out["token_name"] = str(child_token_name.text or "")
    child_not_after = el.find("notAfter")
    if child_not_after is not None:
        import capo_ec2.types.millisecond_date_time

        out["not_after"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_not_after
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.token_state

        out["status"] = capo_ec2.types.token_state.deserialize_ec2_query(child_status)
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.ipam_external_resource_verification_token_state

        out["state"] = (
            capo_ec2.types.ipam_external_resource_verification_token_state.deserialize_ec2_query(
                child_state
            )
        )
    return out

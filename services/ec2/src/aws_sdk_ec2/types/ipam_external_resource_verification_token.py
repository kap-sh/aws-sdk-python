"""Generated from Smithy shape ``com.amazonaws.ec2#IpamExternalResourceVerificationToken``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_id
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_state
    import aws_sdk_ec2.types.ipam_id
    import aws_sdk_ec2.types.millisecond_date_time
    import aws_sdk_ec2.types.resource_arn
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_list
    import aws_sdk_ec2.types.token_state


class IpamExternalResourceVerificationToken(TypedDict):
    ipam_external_resource_verification_token_id: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>The ID of the token.</p>"""
    ipam_external_resource_verification_token_arn: NotRequired[
        "aws_sdk_ec2.types.resource_arn.ResourceArn"
    ]
    """<p>Token ARN.</p>"""
    ipam_id: NotRequired["aws_sdk_ec2.types.ipam_id.IpamId"]
    """<p>The ID of the IPAM that created the token.</p>"""
    ipam_arn: NotRequired["aws_sdk_ec2.types.resource_arn.ResourceArn"]
    """<p>ARN of the IPAM that created the token.</p>"""
    ipam_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Region of the IPAM that created the token.</p>"""
    token_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Token value.</p>"""
    token_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Token name.</p>"""
    not_after: NotRequired[
        "aws_sdk_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Token expiration.</p>"""
    status: NotRequired["aws_sdk_ec2.types.token_state.TokenState"]
    """<p>Token status.</p>"""
    tags: NotRequired["aws_sdk_ec2.types.tag_list.TagList"]
    """<p>Token tags.</p>"""
    state: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_state.IpamExternalResourceVerificationTokenState"
    ]
    """<p>Token state.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamExternalResourceVerificationToken,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_external_resource_verification_token_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamExternalResourceVerificationTokenId",
                str(value["ipam_external_resource_verification_token_id"]),
            )
        )
    if "ipam_external_resource_verification_token_arn" in value:
        pairs.append(
            (
                f"{prefix}.IpamExternalResourceVerificationTokenArn",
                str(value["ipam_external_resource_verification_token_arn"]),
            )
        )
    if "ipam_id" in value:
        pairs.append((f"{prefix}.IpamId", str(value["ipam_id"])))
    if "ipam_arn" in value:
        pairs.append((f"{prefix}.IpamArn", str(value["ipam_arn"])))
    if "ipam_region" in value:
        pairs.append((f"{prefix}.IpamRegion", str(value["ipam_region"])))
    if "token_value" in value:
        pairs.append((f"{prefix}.TokenValue", str(value["token_value"])))
    if "token_name" in value:
        pairs.append((f"{prefix}.TokenName", str(value["token_name"])))
    if "not_after" in value:
        import aws_sdk_ec2.types.millisecond_date_time

        aws_sdk_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["not_after"], pairs, f"{prefix}.NotAfter"
        )
    if "status" in value:
        import aws_sdk_ec2.types.token_state

        aws_sdk_ec2.types.token_state.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "tags" in value:
        import aws_sdk_ec2.types.tag_list

        aws_sdk_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{prefix}.TagSet"
        )
    if "state" in value:
        import aws_sdk_ec2.types.ipam_external_resource_verification_token_state

        aws_sdk_ec2.types.ipam_external_resource_verification_token_state.serialize_ec2_query(
            value["state"], pairs, f"{prefix}.State"
        )


def deserialize_ec2_query(el: Element) -> IpamExternalResourceVerificationToken:
    out: IpamExternalResourceVerificationToken = {}  # type: ignore[typeddict-item]
    child_ipam_external_resource_verification_token_id = el.find(
        "IpamExternalResourceVerificationTokenId"
    )
    if child_ipam_external_resource_verification_token_id is not None:
        out["ipam_external_resource_verification_token_id"] = str(
            child_ipam_external_resource_verification_token_id.text or ""
        )
    child_ipam_external_resource_verification_token_arn = el.find(
        "IpamExternalResourceVerificationTokenArn"
    )
    if child_ipam_external_resource_verification_token_arn is not None:
        out["ipam_external_resource_verification_token_arn"] = str(
            child_ipam_external_resource_verification_token_arn.text or ""
        )
    child_ipam_id = el.find("IpamId")
    if child_ipam_id is not None:
        out["ipam_id"] = str(child_ipam_id.text or "")
    child_ipam_arn = el.find("IpamArn")
    if child_ipam_arn is not None:
        out["ipam_arn"] = str(child_ipam_arn.text or "")
    child_ipam_region = el.find("IpamRegion")
    if child_ipam_region is not None:
        out["ipam_region"] = str(child_ipam_region.text or "")
    child_token_value = el.find("TokenValue")
    if child_token_value is not None:
        out["token_value"] = str(child_token_value.text or "")
    child_token_name = el.find("TokenName")
    if child_token_name is not None:
        out["token_name"] = str(child_token_name.text or "")
    child_not_after = el.find("NotAfter")
    if child_not_after is not None:
        import aws_sdk_ec2.types.millisecond_date_time

        out["not_after"] = (
            aws_sdk_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_not_after
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.token_state

        out["status"] = aws_sdk_ec2.types.token_state.deserialize_ec2_query(
            child_status
        )
    if el.find("TagSet") is not None:
        import aws_sdk_ec2.types.tag_list

        out["tags"] = aws_sdk_ec2.types.tag_list.deserialize_ec2_query(el, "TagSet")
    child_state = el.find("State")
    if child_state is not None:
        import aws_sdk_ec2.types.ipam_external_resource_verification_token_state

        out["state"] = (
            aws_sdk_ec2.types.ipam_external_resource_verification_token_state.deserialize_ec2_query(
                child_state
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudformation#DescribePublisherOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.identity_provider
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.publisher_profile
    import capo_cloudformation.types.publisher_status


class DescribePublisherOutput(TypedDict, closed=True):
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The ID of the extension publisher.</p>"""
    publisher_status: NotRequired[
        "capo_cloudformation.types.publisher_status.PublisherStatus"
    ]
    """<p>Whether the publisher is verified. Currently, all registered publishers are verified.</p>"""
    identity_provider: NotRequired[
        "capo_cloudformation.types.identity_provider.IdentityProvider"
    ]
    """<p>The type of account used as the identity provider when registering this publisher with CloudFormation.</p>"""
    publisher_profile: NotRequired[
        "capo_cloudformation.types.publisher_profile.PublisherProfile"
    ]
    """<p>The URL to the publisher's profile with the identity provider.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePublisherOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "publisher_id" in value:
        pairs.append((f"{key_prefix}PublisherId", str(value["publisher_id"])))
    if "publisher_status" in value:
        import capo_cloudformation.types.publisher_status

        capo_cloudformation.types.publisher_status.serialize_query(
            value["publisher_status"], pairs, f"{key_prefix}PublisherStatus"
        )
    if "identity_provider" in value:
        import capo_cloudformation.types.identity_provider

        capo_cloudformation.types.identity_provider.serialize_query(
            value["identity_provider"], pairs, f"{key_prefix}IdentityProvider"
        )
    if "publisher_profile" in value:
        pairs.append((f"{key_prefix}PublisherProfile", str(value["publisher_profile"])))


def deserialize_query(el: Element) -> DescribePublisherOutput:
    out: DescribePublisherOutput = {}  # type: ignore[typeddict-item]
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_publisher_status = el.find("PublisherStatus")
    if child_publisher_status is not None:
        import capo_cloudformation.types.publisher_status

        out["publisher_status"] = (
            capo_cloudformation.types.publisher_status.deserialize_query(
                child_publisher_status
            )
        )
    child_identity_provider = el.find("IdentityProvider")
    if child_identity_provider is not None:
        import capo_cloudformation.types.identity_provider

        out["identity_provider"] = (
            capo_cloudformation.types.identity_provider.deserialize_query(
                child_identity_provider
            )
        )
    child_publisher_profile = el.find("PublisherProfile")
    if child_publisher_profile is not None:
        out["publisher_profile"] = str(child_publisher_profile.text or "")
    return out

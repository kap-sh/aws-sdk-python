"""Generated from Smithy shape ``com.amazonaws.iam#ListSSHPublicKeysResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.boolean_type
    import capo_iam.types.response_marker_type
    import capo_iam.types.ssh_public_key_list_type


class ListSSHPublicKeysResponse(TypedDict, closed=True):
    ssh_public_keys: NotRequired[
        "capo_iam.types.ssh_public_key_list_type.SSHPublicKeyListType"
    ]
    """<p>A list of the SSH public keys assigned to IAM user.</p>"""
    is_truncated: "capo_iam.types.boolean_type.booleanType"
    """<p>A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the <code>Marker</code> request parameter to retrieve more items. Note that IAM might return fewer than the <code>MaxItems</code> number of results even when there are more results available. We recommend that you check <code>IsTruncated</code> after every call to ensure that you receive all your results.</p>"""
    marker: NotRequired["capo_iam.types.response_marker_type.responseMarkerType"]
    """<p>When <code>IsTruncated</code> is <code>true</code>, this element is present and contains the value to use for the <code>Marker</code> parameter in a subsequent pagination request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListSSHPublicKeysResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ssh_public_keys" in value:
        import capo_iam.types.ssh_public_key_list_type

        capo_iam.types.ssh_public_key_list_type.serialize_query(
            value["ssh_public_keys"], pairs, f"{key_prefix}SSHPublicKeys"
        )
    pairs.append(
        (
            f"{key_prefix}IsTruncated",
            "true" if value.get("is_truncated", False) else "false",
        )
    )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> ListSSHPublicKeysResponse:
    out: ListSSHPublicKeysResponse = {}  # type: ignore[typeddict-item]
    child_ssh_public_keys = el.find("SSHPublicKeys")
    if child_ssh_public_keys is not None:
        import capo_iam.types.ssh_public_key_list_type

        out["ssh_public_keys"] = (
            capo_iam.types.ssh_public_key_list_type.deserialize_query(
                child_ssh_public_keys
            )
        )
    child_is_truncated = el.find("IsTruncated")
    if child_is_truncated is not None:
        out["is_truncated"] = (child_is_truncated.text or "").lower() == "true"
    else:
        out["is_truncated"] = False
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out

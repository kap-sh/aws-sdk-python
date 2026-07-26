"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#AssociateRepositoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeguru_reviewer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.client_request_token
    import capo_codeguru_reviewer.types.kms_key_details
    import capo_codeguru_reviewer.types.repository
    import capo_codeguru_reviewer.types.tag_map


class AssociateRepositoryRequest(TypedDict, closed=True):
    repository: "capo_codeguru_reviewer.types.repository.Repository"
    """<p>The repository to associate.</p>"""
    client_request_token: NotRequired[
        "capo_codeguru_reviewer.types.client_request_token.ClientRequestToken"
    ]
    """<p>Amazon CodeGuru Reviewer uses this value to prevent the accidental creation of duplicate repository associations if there are failures and retries.</p>"""
    tags: NotRequired["capo_codeguru_reviewer.types.tag_map.TagMap"]
    """<p>An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:</p> <ul> <li> <p>A <i>tag key</i> (for example, <code>CostCenter</code>, <code>Environment</code>, <code>Project</code>, or <code>Secret</code>). Tag keys are case sensitive.</p> </li> <li> <p>An optional field known as a <i>tag value</i> (for example, <code>111122223333</code>, <code>Production</code>, or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.</p> </li> </ul>"""
    kms_key_details: NotRequired[
        "capo_codeguru_reviewer.types.kms_key_details.KMSKeyDetails"
    ]
    """<p>A <code>KMSKeyDetails</code> object that contains:</p> <ul> <li> <p>The encryption option for this repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (<code>AWS_OWNED_CMK</code>) or customer managed (<code>CUSTOMER_MANAGED_CMK</code>).</p> </li> <li> <p>The ID of the Amazon Web Services KMS key that is associated with this repository association.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateRepositoryRequest) -> dict:
    out: dict = {}
    import capo_codeguru_reviewer.types.repository

    out["Repository"] = capo_codeguru_reviewer.types.repository.serialize_json(
        value["repository"]
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_codeguru_reviewer.types.tag_map

        out["Tags"] = capo_codeguru_reviewer.types.tag_map.serialize_json(value["tags"])
    if "kms_key_details" in value:
        import capo_codeguru_reviewer.types.kms_key_details

        out["KMSKeyDetails"] = (
            capo_codeguru_reviewer.types.kms_key_details.serialize_json(
                value["kms_key_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateRepositoryRequest:
    out: AssociateRepositoryRequest = {}  # type: ignore[typeddict-item]
    if "Repository" in data:
        import capo_codeguru_reviewer.types.repository

        out["repository"] = capo_codeguru_reviewer.types.repository.deserialize_json(
            data["Repository"]
        )
    else:
        raise DeserializationError("AssociateRepositoryRequest.repository required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import capo_codeguru_reviewer.types.tag_map

        out["tags"] = capo_codeguru_reviewer.types.tag_map.deserialize_json(
            data["Tags"]
        )
    if "KMSKeyDetails" in data:
        import capo_codeguru_reviewer.types.kms_key_details

        out["kms_key_details"] = (
            capo_codeguru_reviewer.types.kms_key_details.deserialize_json(
                data["KMSKeyDetails"]
            )
        )
    return out

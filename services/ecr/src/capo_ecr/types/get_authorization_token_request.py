"""Generated from Smithy shape ``com.amazonaws.ecr#GetAuthorizationTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.get_authorization_token_registry_id_list


class GetAuthorizationTokenRequest(TypedDict, closed=True):
    registry_ids: NotRequired[
        "capo_ecr.types.get_authorization_token_registry_id_list.GetAuthorizationTokenRegistryIdList"
    ]
    """<p>A list of Amazon Web Services account IDs that are associated with the registries for which to get AuthorizationData objects. If you do not specify a registry, the default registry is assumed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAuthorizationTokenRequest) -> dict:
    out: dict = {}
    if "registry_ids" in value:
        import capo_ecr.types.get_authorization_token_registry_id_list

        out["registryIds"] = (
            capo_ecr.types.get_authorization_token_registry_id_list.serialize_aws_json_1_1(
                value["registry_ids"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAuthorizationTokenRequest:
    out: GetAuthorizationTokenRequest = {}  # type: ignore[typeddict-item]
    if "registryIds" in data:
        import capo_ecr.types.get_authorization_token_registry_id_list

        out["registry_ids"] = (
            capo_ecr.types.get_authorization_token_registry_id_list.deserialize_aws_json_1_1(
                data["registryIds"]
            )
        )
    return out

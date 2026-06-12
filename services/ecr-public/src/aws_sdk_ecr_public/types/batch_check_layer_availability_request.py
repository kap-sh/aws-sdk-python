"""Generated from Smithy shape ``com.amazonaws.ecrpublic#BatchCheckLayerAvailabilityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr_public.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.batched_operation_layer_digest_list
    import aws_sdk_ecr_public.types.registry_id_or_alias
    import aws_sdk_ecr_public.types.repository_name


class BatchCheckLayerAvailabilityRequest(TypedDict):
    registry_id: NotRequired[
        "aws_sdk_ecr_public.types.registry_id_or_alias.RegistryIdOrAlias"
    ]
    """<p>The Amazon Web Services account ID, or registry alias, associated with the public registry that contains the image layers to check. If you do not specify a registry, the default public registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    """<p>The name of the repository that's associated with the image layers to check.</p>"""
    layer_digests: "aws_sdk_ecr_public.types.batched_operation_layer_digest_list.BatchedOperationLayerDigestList"
    """<p>The digests of the image layers to check.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchCheckLayerAvailabilityRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import aws_sdk_ecr_public.types.batched_operation_layer_digest_list

    out["layerDigests"] = (
        aws_sdk_ecr_public.types.batched_operation_layer_digest_list.serialize_aws_json_1_1(
            value["layer_digests"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchCheckLayerAvailabilityRequest:
    out: BatchCheckLayerAvailabilityRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "BatchCheckLayerAvailabilityRequest.repository_name required"
        )
    if "layerDigests" in data:
        import aws_sdk_ecr_public.types.batched_operation_layer_digest_list

        out["layer_digests"] = (
            aws_sdk_ecr_public.types.batched_operation_layer_digest_list.deserialize_aws_json_1_1(
                data["layerDigests"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCheckLayerAvailabilityRequest.layer_digests required"
        )
    return out

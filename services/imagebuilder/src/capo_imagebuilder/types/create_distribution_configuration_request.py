"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateDistributionConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.distribution_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map


class CreateDistributionConfigurationRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the distribution configuration.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the distribution configuration.</p>"""
    distributions: "capo_imagebuilder.types.distribution_list.DistributionList"
    """<p>The distributions of the distribution configuration.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the distribution configuration.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    r"""<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDistributionConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_imagebuilder.types.distribution_list

    out["distributions"] = capo_imagebuilder.types.distribution_list.serialize_json(
        value["distributions"]
    )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateDistributionConfigurationRequest:
    out: CreateDistributionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateDistributionConfigurationRequest.name required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "distributions" in data:
        import capo_imagebuilder.types.distribution_list

        out["distributions"] = (
            capo_imagebuilder.types.distribution_list.deserialize_json(
                data["distributions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDistributionConfigurationRequest.distributions required"
        )
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateDistributionConfigurationRequest.client_token required"
        )
    return out

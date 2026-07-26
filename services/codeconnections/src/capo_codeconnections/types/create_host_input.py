"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateHostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeconnections.types.host_name
    import capo_codeconnections.types.provider_type
    import capo_codeconnections.types.tag_list
    import capo_codeconnections.types.url
    import capo_codeconnections.types.vpc_configuration


class CreateHostInput(TypedDict, closed=True):
    name: "capo_codeconnections.types.host_name.HostName"
    """<p>The name of the host to be created.</p>"""
    provider_type: "capo_codeconnections.types.provider_type.ProviderType"
    """<p>The name of the installed provider to be associated with your connection. The host resource represents the infrastructure where your provider type is installed. The valid provider type is GitHub Enterprise Server.</p>"""
    provider_endpoint: "capo_codeconnections.types.url.Url"
    """<p>The endpoint of the infrastructure to be represented by the host after it is created.</p>"""
    vpc_configuration: NotRequired[
        "capo_codeconnections.types.vpc_configuration.VpcConfiguration"
    ]
    """<p>The VPC configuration to be provisioned for the host. A VPC must be configured and the infrastructure to be represented by the host must already be connected to the VPC.</p>"""
    tags: NotRequired["capo_codeconnections.types.tag_list.TagList"]
    """<p>Tags for the host to be created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateHostInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_codeconnections.types.provider_type

    out["ProviderType"] = (
        capo_codeconnections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["ProviderEndpoint"] = value["provider_endpoint"]
    if "vpc_configuration" in value:
        import capo_codeconnections.types.vpc_configuration

        out["VpcConfiguration"] = (
            capo_codeconnections.types.vpc_configuration.serialize_aws_json_1_0(
                value["vpc_configuration"]
            )
        )
    if "tags" in value:
        import capo_codeconnections.types.tag_list

        out["Tags"] = capo_codeconnections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateHostInput:
    out: CreateHostInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateHostInput.name required")
    if "ProviderType" in data:
        import capo_codeconnections.types.provider_type

        out["provider_type"] = (
            capo_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        raise DeserializationError("CreateHostInput.provider_type required")
    if "ProviderEndpoint" in data:
        out["provider_endpoint"] = data["ProviderEndpoint"]
    else:
        raise DeserializationError("CreateHostInput.provider_endpoint required")
    if "VpcConfiguration" in data:
        import capo_codeconnections.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_codeconnections.types.vpc_configuration.deserialize_aws_json_1_0(
                data["VpcConfiguration"]
            )
        )
    if "Tags" in data:
        import capo_codeconnections.types.tag_list

        out["tags"] = capo_codeconnections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out

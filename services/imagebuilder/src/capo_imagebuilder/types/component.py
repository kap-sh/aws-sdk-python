"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Component``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.component_data
    import capo_imagebuilder.types.component_parameter_detail_list
    import capo_imagebuilder.types.component_state
    import capo_imagebuilder.types.component_type
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.os_version_list
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.product_code_list
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.version_number


class Component(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the component.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The version of the component.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the component.</p>"""
    change_description: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes what change has been made in this version of the component, or what makes this version different from other versions of the component.</p>"""
    type: NotRequired["capo_imagebuilder.types.component_type.ComponentType"]
    """<p>The component type specifies whether Image Builder uses the component to build the image or only to test it.</p>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The operating system platform of the component.</p>"""
    supported_os_versions: NotRequired[
        "capo_imagebuilder.types.os_version_list.OsVersionList"
    ]
    """<p>The operating system (OS) version supported by the component. If the OS information is available, Image Builder performs a prefix match against the base image OS version during image recipe creation.</p>"""
    state: NotRequired["capo_imagebuilder.types.component_state.ComponentState"]
    """<p>Describes the current status of the component.</p>"""
    parameters: NotRequired[
        "capo_imagebuilder.types.component_parameter_detail_list.ComponentParameterDetailList"
    ]
    """<p>Contains parameter details for each of the parameters that the component document defined for the component.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the component.</p>"""
    data: NotRequired["capo_imagebuilder.types.component_data.ComponentData"]
    """<p>Component data contains the YAML document content for the component.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    r"""<p>The KMS key identifier used to encrypt the component. This can be either the Key ARN or the Alias ARN. For more information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    encrypted: NotRequired["capo_imagebuilder.types.nullable_boolean.NullableBoolean"]
    """<p>The encryption status of the component.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date that Image Builder created the component.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags that apply to the component.</p>"""
    publisher: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Contains the name of the publisher if this is a third-party component. Otherwise, this property is empty.</p>"""
    obfuscate: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Indicates whether component source is hidden from view in the console, and from component detail results for API, CLI, or SDK operations.</p>"""
    product_codes: NotRequired[
        "capo_imagebuilder.types.product_code_list.ProductCodeList"
    ]
    """<p>Contains product codes that are used for billing purposes for Amazon Web Services Marketplace components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Component) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "description" in value:
        out["description"] = value["description"]
    if "change_description" in value:
        out["changeDescription"] = value["change_description"]
    if "type" in value:
        import capo_imagebuilder.types.component_type

        out["type"] = capo_imagebuilder.types.component_type.serialize_json(
            value["type"]
        )
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "supported_os_versions" in value:
        import capo_imagebuilder.types.os_version_list

        out["supportedOsVersions"] = (
            capo_imagebuilder.types.os_version_list.serialize_json(
                value["supported_os_versions"]
            )
        )
    if "state" in value:
        import capo_imagebuilder.types.component_state

        out["state"] = capo_imagebuilder.types.component_state.serialize_json(
            value["state"]
        )
    if "parameters" in value:
        import capo_imagebuilder.types.component_parameter_detail_list

        out["parameters"] = (
            capo_imagebuilder.types.component_parameter_detail_list.serialize_json(
                value["parameters"]
            )
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "data" in value:
        out["data"] = value["data"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "publisher" in value:
        out["publisher"] = value["publisher"]
    out["obfuscate"] = value.get("obfuscate", False)
    if "product_codes" in value:
        import capo_imagebuilder.types.product_code_list

        out["productCodes"] = capo_imagebuilder.types.product_code_list.serialize_json(
            value["product_codes"]
        )
    return out


def deserialize_json(data: dict) -> Component:
    out: Component = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "description" in data:
        out["description"] = data["description"]
    if "changeDescription" in data:
        out["change_description"] = data["changeDescription"]
    if "type" in data:
        import capo_imagebuilder.types.component_type

        out["type"] = capo_imagebuilder.types.component_type.deserialize_json(
            data["type"]
        )
    if "platform" in data:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if "supportedOsVersions" in data:
        import capo_imagebuilder.types.os_version_list

        out["supported_os_versions"] = (
            capo_imagebuilder.types.os_version_list.deserialize_json(
                data["supportedOsVersions"]
            )
        )
    if "state" in data:
        import capo_imagebuilder.types.component_state

        out["state"] = capo_imagebuilder.types.component_state.deserialize_json(
            data["state"]
        )
    if "parameters" in data:
        import capo_imagebuilder.types.component_parameter_detail_list

        out["parameters"] = (
            capo_imagebuilder.types.component_parameter_detail_list.deserialize_json(
                data["parameters"]
            )
        )
    if "owner" in data:
        out["owner"] = data["owner"]
    if "data" in data:
        out["data"] = data["data"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "encrypted" in data:
        out["encrypted"] = data["encrypted"]
    if "dateCreated" in data:
        out["date_created"] = data["dateCreated"]
    if "tags" in data:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if "publisher" in data:
        out["publisher"] = data["publisher"]
    if "obfuscate" in data:
        out["obfuscate"] = data["obfuscate"]
    else:
        out["obfuscate"] = False
    if "productCodes" in data:
        import capo_imagebuilder.types.product_code_list

        out["product_codes"] = (
            capo_imagebuilder.types.product_code_list.deserialize_json(
                data["productCodes"]
            )
        )
    return out

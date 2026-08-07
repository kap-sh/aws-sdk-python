"""Generated from Smithy shape ``com.amazonaws.cloudformation#ActivateTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.auto_update
    import capo_cloudformation.types.logging_config
    import capo_cloudformation.types.major_version
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.role_arn2
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.third_party_type_arn
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.version_bump


class ActivateTypeInput(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.third_party_type.ThirdPartyType"]
    """<p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>"""
    public_type_arn: NotRequired[
        "capo_cloudformation.types.third_party_type_arn.ThirdPartyTypeArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>"""
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>"""
    type_name_alias: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>An alias to assign to the public extension in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.</p>"""
    auto_update: NotRequired["capo_cloudformation.types.auto_update.AutoUpdate"]
    """<p>Whether to automatically update the extension in this account and Region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>"""
    logging_config: NotRequired[
        "capo_cloudformation.types.logging_config.LoggingConfig"
    ]
    """<p>Contains logging configuration information for an extension.</p>"""
    execution_role_arn: NotRequired["capo_cloudformation.types.role_arn2.RoleARN2"]
    """<p>The name of the IAM execution role to use to activate the extension.</p>"""
    version_bump: NotRequired["capo_cloudformation.types.version_bump.VersionBump"]
    """<p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>"""
    major_version: NotRequired["capo_cloudformation.types.major_version.MajorVersion"]
    """<p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ActivateTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.third_party_type

        capo_cloudformation.types.third_party_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "public_type_arn" in value:
        pairs.append((f"{key_prefix}PublicTypeArn", str(value["public_type_arn"])))
    if "publisher_id" in value:
        pairs.append((f"{key_prefix}PublisherId", str(value["publisher_id"])))
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "type_name_alias" in value:
        pairs.append((f"{key_prefix}TypeNameAlias", str(value["type_name_alias"])))
    if "auto_update" in value:
        pairs.append(
            (f"{key_prefix}AutoUpdate", "true" if value["auto_update"] else "false")
        )
    if "logging_config" in value:
        import capo_cloudformation.types.logging_config

        capo_cloudformation.types.logging_config.serialize_query(
            value["logging_config"], pairs, f"{key_prefix}LoggingConfig"
        )
    if "execution_role_arn" in value:
        pairs.append(
            (f"{key_prefix}ExecutionRoleArn", str(value["execution_role_arn"]))
        )
    if "version_bump" in value:
        import capo_cloudformation.types.version_bump

        capo_cloudformation.types.version_bump.serialize_query(
            value["version_bump"], pairs, f"{key_prefix}VersionBump"
        )
    if "major_version" in value:
        pairs.append((f"{key_prefix}MajorVersion", str(value["major_version"])))


def deserialize_query(el: Element) -> ActivateTypeInput:
    out: ActivateTypeInput = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.third_party_type

        out["type"] = capo_cloudformation.types.third_party_type.deserialize_query(
            child_type
        )
    child_public_type_arn = el.find("PublicTypeArn")
    if child_public_type_arn is not None:
        out["public_type_arn"] = str(child_public_type_arn.text or "")
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_type_name_alias = el.find("TypeNameAlias")
    if child_type_name_alias is not None:
        out["type_name_alias"] = str(child_type_name_alias.text or "")
    child_auto_update = el.find("AutoUpdate")
    if child_auto_update is not None:
        out["auto_update"] = (child_auto_update.text or "").lower() == "true"
    child_logging_config = el.find("LoggingConfig")
    if child_logging_config is not None:
        import capo_cloudformation.types.logging_config

        out["logging_config"] = (
            capo_cloudformation.types.logging_config.deserialize_query(
                child_logging_config
            )
        )
    child_execution_role_arn = el.find("ExecutionRoleArn")
    if child_execution_role_arn is not None:
        out["execution_role_arn"] = str(child_execution_role_arn.text or "")
    child_version_bump = el.find("VersionBump")
    if child_version_bump is not None:
        import capo_cloudformation.types.version_bump

        out["version_bump"] = capo_cloudformation.types.version_bump.deserialize_query(
            child_version_bump
        )
    child_major_version = el.find("MajorVersion")
    if child_major_version is not None:
        out["major_version"] = int(child_major_version.text or "")
    return out

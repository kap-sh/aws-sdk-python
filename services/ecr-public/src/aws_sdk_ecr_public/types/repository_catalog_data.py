"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryCatalogData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.about_text
    import aws_sdk_ecr_public.types.architecture_list
    import aws_sdk_ecr_public.types.marketplace_certified
    import aws_sdk_ecr_public.types.operating_system_list
    import aws_sdk_ecr_public.types.repository_description
    import aws_sdk_ecr_public.types.resource_url
    import aws_sdk_ecr_public.types.usage_text


class RepositoryCatalogData(TypedDict):
    description: NotRequired[
        "aws_sdk_ecr_public.types.repository_description.RepositoryDescription"
    ]
    """<p>The short description of the repository.</p>"""
    architectures: NotRequired[
        "aws_sdk_ecr_public.types.architecture_list.ArchitectureList"
    ]
    """<p>The architecture tags that are associated with the repository.</p> <note> <p>Only supported operating system tags appear publicly in the Amazon ECR Public Gallery. For more information, see <a>RepositoryCatalogDataInput</a>.</p> </note>"""
    operating_systems: NotRequired[
        "aws_sdk_ecr_public.types.operating_system_list.OperatingSystemList"
    ]
    """<p>The operating system tags that are associated with the repository.</p> <note> <p>Only supported operating system tags appear publicly in the Amazon ECR Public Gallery. For more information, see <a>RepositoryCatalogDataInput</a>.</p> </note>"""
    logo_url: NotRequired["aws_sdk_ecr_public.types.resource_url.ResourceUrl"]
    """<p>The URL that contains the logo that's associated with the repository.</p>"""
    about_text: NotRequired["aws_sdk_ecr_public.types.about_text.AboutText"]
    """<p>The longform description of the contents of the repository. This text appears in the repository details on the Amazon ECR Public Gallery.</p>"""
    usage_text: NotRequired["aws_sdk_ecr_public.types.usage_text.UsageText"]
    """<p>The longform usage details of the contents of the repository. The usage text provides context for users of the repository.</p>"""
    marketplace_certified: NotRequired[
        "aws_sdk_ecr_public.types.marketplace_certified.MarketplaceCertified"
    ]
    """<p>Indicates whether the repository is certified by Amazon Web Services Marketplace.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryCatalogData) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "architectures" in value:
        import aws_sdk_ecr_public.types.architecture_list

        out["architectures"] = (
            aws_sdk_ecr_public.types.architecture_list.serialize_aws_json_1_1(
                value["architectures"]
            )
        )
    if "operating_systems" in value:
        import aws_sdk_ecr_public.types.operating_system_list

        out["operatingSystems"] = (
            aws_sdk_ecr_public.types.operating_system_list.serialize_aws_json_1_1(
                value["operating_systems"]
            )
        )
    if "logo_url" in value:
        out["logoUrl"] = value["logo_url"]
    if "about_text" in value:
        out["aboutText"] = value["about_text"]
    if "usage_text" in value:
        out["usageText"] = value["usage_text"]
    if "marketplace_certified" in value:
        out["marketplaceCertified"] = value["marketplace_certified"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryCatalogData:
    out: RepositoryCatalogData = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "architectures" in data:
        import aws_sdk_ecr_public.types.architecture_list

        out["architectures"] = (
            aws_sdk_ecr_public.types.architecture_list.deserialize_aws_json_1_1(
                data["architectures"]
            )
        )
    if "operatingSystems" in data:
        import aws_sdk_ecr_public.types.operating_system_list

        out["operating_systems"] = (
            aws_sdk_ecr_public.types.operating_system_list.deserialize_aws_json_1_1(
                data["operatingSystems"]
            )
        )
    if "logoUrl" in data:
        out["logo_url"] = data["logoUrl"]
    if "aboutText" in data:
        out["about_text"] = data["aboutText"]
    if "usageText" in data:
        out["usage_text"] = data["usageText"]
    if "marketplaceCertified" in data:
        out["marketplace_certified"] = data["marketplaceCertified"]
    return out

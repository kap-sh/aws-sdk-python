"""Generated from Smithy shape ``com.amazonaws.ecrpublic#RepositoryCatalogDataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr_public.types.about_text
    import capo_ecr_public.types.architecture_list
    import capo_ecr_public.types.logo_image_blob
    import capo_ecr_public.types.operating_system_list
    import capo_ecr_public.types.repository_description
    import capo_ecr_public.types.usage_text


class RepositoryCatalogDataInput(TypedDict, closed=True):
    description: NotRequired[
        "capo_ecr_public.types.repository_description.RepositoryDescription"
    ]
    """<p>A short description of the contents of the repository. This text appears in both the image details and also when searching for repositories on the Amazon ECR Public Gallery.</p>"""
    architectures: NotRequired[
        "capo_ecr_public.types.architecture_list.ArchitectureList"
    ]
    """<p>The system architecture that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported architectures appear as badges on the repository and are used as search filters.</p> <note> <p>If an unsupported tag is added to your repository catalog data, it's associated with the repository and can be retrieved using the API but isn't discoverable in the Amazon ECR Public Gallery.</p> </note> <ul> <li> <p> <code>ARM</code> </p> </li> <li> <p> <code>ARM 64</code> </p> </li> <li> <p> <code>x86</code> </p> </li> <li> <p> <code>x86-64</code> </p> </li> </ul>"""
    operating_systems: NotRequired[
        "capo_ecr_public.types.operating_system_list.OperatingSystemList"
    ]
    """<p>The operating systems that the images in the repository are compatible with. On the Amazon ECR Public Gallery, the following supported operating systems appear as badges on the repository and are used as search filters.</p> <note> <p>If an unsupported tag is added to your repository catalog data, it's associated with the repository and can be retrieved using the API but isn't discoverable in the Amazon ECR Public Gallery.</p> </note> <ul> <li> <p> <code>Linux</code> </p> </li> <li> <p> <code>Windows</code> </p> </li> </ul>"""
    logo_image_blob: NotRequired["capo_ecr_public.types.logo_image_blob.LogoImageBlob"]
    """<p>The base64-encoded repository logo payload.</p> <note> <p>The repository logo is only publicly visible in the Amazon ECR Public Gallery for verified accounts.</p> </note>"""
    about_text: NotRequired["capo_ecr_public.types.about_text.AboutText"]
    """<p>A detailed description of the contents of the repository. It's publicly visible in the Amazon ECR Public Gallery. The text must be in markdown format.</p>"""
    usage_text: NotRequired["capo_ecr_public.types.usage_text.UsageText"]
    """<p>Detailed information about how to use the contents of the repository. It's publicly visible in the Amazon ECR Public Gallery. The usage text provides context, support information, and additional usage details for users of the repository. The text must be in markdown format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryCatalogDataInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "architectures" in value:
        import capo_ecr_public.types.architecture_list

        out["architectures"] = (
            capo_ecr_public.types.architecture_list.serialize_aws_json_1_1(
                value["architectures"]
            )
        )
    if "operating_systems" in value:
        import capo_ecr_public.types.operating_system_list

        out["operatingSystems"] = (
            capo_ecr_public.types.operating_system_list.serialize_aws_json_1_1(
                value["operating_systems"]
            )
        )
    if "logo_image_blob" in value:
        import capo_ecr_public.types.logo_image_blob

        out["logoImageBlob"] = (
            capo_ecr_public.types.logo_image_blob.serialize_aws_json_1_1(
                value["logo_image_blob"]
            )
        )
    if "about_text" in value:
        out["aboutText"] = value["about_text"]
    if "usage_text" in value:
        out["usageText"] = value["usage_text"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryCatalogDataInput:
    out: RepositoryCatalogDataInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "architectures" in data:
        import capo_ecr_public.types.architecture_list

        out["architectures"] = (
            capo_ecr_public.types.architecture_list.deserialize_aws_json_1_1(
                data["architectures"]
            )
        )
    if "operatingSystems" in data:
        import capo_ecr_public.types.operating_system_list

        out["operating_systems"] = (
            capo_ecr_public.types.operating_system_list.deserialize_aws_json_1_1(
                data["operatingSystems"]
            )
        )
    if "logoImageBlob" in data:
        import capo_ecr_public.types.logo_image_blob

        out["logo_image_blob"] = (
            capo_ecr_public.types.logo_image_blob.deserialize_aws_json_1_1(
                data["logoImageBlob"]
            )
        )
    if "aboutText" in data:
        out["about_text"] = data["aboutText"]
    if "usageText" in data:
        out["usage_text"] = data["usageText"]
    return out

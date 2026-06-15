"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#CreateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__list_of__string
    import aws_sdk_serverlessapplicationrepository.types.__string


class CreateApplicationRequest(TypedDict):
    author: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    r"""<p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";</p>"""
    description: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The description of the application.</p><p>Minimum length=1. Maximum length=256</p>"""
    home_page_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A URL with more information about the application, for example the location of your GitHub repository for the application.</p>"""
    labels: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__list_of__string.__listOf__string"
    ]
    r"""<p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";</p>"""
    license_body: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A local text file that contains the license of the app that matches the spdxLicenseID value of your application. The file has the format file://&lt;path>/&lt;filename>.</p><p>Maximum size 5 MB</p><p>You can specify only one of licenseBody and licenseUrl; otherwise, an error results.</p>"""
    license_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the S3 object that contains the license of the app that matches the spdxLicenseID value of your application.</p><p>Maximum size 5 MB</p><p>You can specify only one of licenseBody and licenseUrl; otherwise, an error results.</p>"""
    name: NotRequired["aws_sdk_serverlessapplicationrepository.types.__string.__string"]
    r"""<p>The name of the application that you want to publish.</p><p>Minimum length=1. Maximum length=140</p><p>Pattern: \"[a-zA-Z0-9\\-]+\";</p>"""
    readme_body: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A local text readme file in Markdown language that contains a more detailed description of the application and how it works. The file has the format file://&lt;path>/&lt;filename>.</p><p>Maximum size 5 MB</p><p>You can specify only one of readmeBody and readmeUrl; otherwise, an error results.</p>"""
    readme_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the S3 object in Markdown language that contains a more detailed description of the application and how it works.</p><p>Maximum size 5 MB</p><p>You can specify only one of readmeBody and readmeUrl; otherwise, an error results.</p>"""
    semantic_version: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    r"""<p>The semantic version of the application:</p><p> <a href=\"https://semver.org/\">https://semver.org/</a> </p>"""
    source_code_archive_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>"""
    source_code_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.</p>"""
    spdx_license_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    r"""<p>A valid identifier from <a href=\"https://spdx.org/licenses/\">https://spdx.org/licenses/</a>.</p>"""
    template_body: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The local raw packaged AWS SAM template file of your application. The file has the format file://&lt;path>/&lt;filename>.</p><p>You can specify only one of templateBody and templateUrl; otherwise an error results.</p>"""
    template_url: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the S3 object containing the packaged AWS SAM template of your application.</p><p>You can specify only one of templateBody and templateUrl; otherwise an error results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    if "author" in value:
        out["author"] = value["author"]
    if "description" in value:
        out["description"] = value["description"]
    if "home_page_url" in value:
        out["homePageUrl"] = value["home_page_url"]
    if "labels" in value:
        import aws_sdk_serverlessapplicationrepository.types.__list_of__string

        out["labels"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of__string.serialize_json(
                value["labels"]
            )
        )
    if "license_body" in value:
        out["licenseBody"] = value["license_body"]
    if "license_url" in value:
        out["licenseUrl"] = value["license_url"]
    if "name" in value:
        out["name"] = value["name"]
    if "readme_body" in value:
        out["readmeBody"] = value["readme_body"]
    if "readme_url" in value:
        out["readmeUrl"] = value["readme_url"]
    if "semantic_version" in value:
        out["semanticVersion"] = value["semantic_version"]
    if "source_code_archive_url" in value:
        out["sourceCodeArchiveUrl"] = value["source_code_archive_url"]
    if "source_code_url" in value:
        out["sourceCodeUrl"] = value["source_code_url"]
    if "spdx_license_id" in value:
        out["spdxLicenseId"] = value["spdx_license_id"]
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    if "template_url" in value:
        out["templateUrl"] = value["template_url"]
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "author" in data:
        out["author"] = data["author"]
    if "description" in data:
        out["description"] = data["description"]
    if "homePageUrl" in data:
        out["home_page_url"] = data["homePageUrl"]
    if "labels" in data:
        import aws_sdk_serverlessapplicationrepository.types.__list_of__string

        out["labels"] = (
            aws_sdk_serverlessapplicationrepository.types.__list_of__string.deserialize_json(
                data["labels"]
            )
        )
    if "licenseBody" in data:
        out["license_body"] = data["licenseBody"]
    if "licenseUrl" in data:
        out["license_url"] = data["licenseUrl"]
    if "name" in data:
        out["name"] = data["name"]
    if "readmeBody" in data:
        out["readme_body"] = data["readmeBody"]
    if "readmeUrl" in data:
        out["readme_url"] = data["readmeUrl"]
    if "semanticVersion" in data:
        out["semantic_version"] = data["semanticVersion"]
    if "sourceCodeArchiveUrl" in data:
        out["source_code_archive_url"] = data["sourceCodeArchiveUrl"]
    if "sourceCodeUrl" in data:
        out["source_code_url"] = data["sourceCodeUrl"]
    if "spdxLicenseId" in data:
        out["spdx_license_id"] = data["spdxLicenseId"]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "templateUrl" in data:
        out["template_url"] = data["templateUrl"]
    return out

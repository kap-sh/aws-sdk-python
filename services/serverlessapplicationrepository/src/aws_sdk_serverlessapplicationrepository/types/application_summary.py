"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#ApplicationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_serverlessapplicationrepository.types.__list_of__string
    import aws_sdk_serverlessapplicationrepository.types.__string


class ApplicationSummary(TypedDict):
    application_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The application Amazon Resource Name (ARN).</p>"""
    author: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The name of the author publishing the app.</p><p>Minimum length=1. Maximum length=127.</p><p>Pattern \"^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\";</p>"""
    creation_time: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The date and time this resource was created.</p>"""
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
    """<p>Labels to improve discovery of apps in search results.</p><p>Minimum length=1. Maximum length=127. Maximum number of labels: 10</p><p>Pattern: \"^[a-zA-Z0-9+\\-_:\\/@]+$\";</p>"""
    name: NotRequired["aws_sdk_serverlessapplicationrepository.types.__string.__string"]
    """<p>The name of the application.</p><p>Minimum length=1. Maximum length=140</p><p>Pattern: \"[a-zA-Z0-9\\-]+\";</p>"""
    spdx_license_id: NotRequired[
        "aws_sdk_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A valid identifier from <a href=\"https://spdx.org/licenses/\">https://spdx.org/licenses/</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationSummary) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "author" in value:
        out["author"] = value["author"]
    if "creation_time" in value:
        out["creationTime"] = value["creation_time"]
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
    if "name" in value:
        out["name"] = value["name"]
    if "spdx_license_id" in value:
        out["spdxLicenseId"] = value["spdx_license_id"]
    return out


def deserialize_json(data: dict) -> ApplicationSummary:
    out: ApplicationSummary = {}  # type: ignore[typeddict-item]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "author" in data:
        out["author"] = data["author"]
    if "creationTime" in data:
        out["creation_time"] = data["creationTime"]
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
    if "name" in data:
        out["name"] = data["name"]
    if "spdxLicenseId" in data:
        out["spdx_license_id"] = data["spdxLicenseId"]
    return out

"""Generated from Smithy shape ``com.amazonaws.serverlessapplicationrepository#CreateApplicationVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_serverlessapplicationrepository.types.__string


class CreateApplicationVersionRequest(TypedDict, closed=True):
    application_id: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    semantic_version: "capo_serverlessapplicationrepository.types.__string.__string"
    """<p>The semantic version of the new version.</p>"""
    source_code_archive_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the S3 object that contains the ZIP archive of the source code for this version of your application.</p><p>Maximum size 50 MB</p>"""
    source_code_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.</p>"""
    template_body: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>The raw packaged AWS SAM template of your application.</p>"""
    template_url: NotRequired[
        "capo_serverlessapplicationrepository.types.__string.__string"
    ]
    """<p>A link to the packaged AWS SAM template of your application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationVersionRequest) -> dict:
    out: dict = {}
    if "source_code_archive_url" in value:
        out["sourceCodeArchiveUrl"] = value["source_code_archive_url"]
    if "source_code_url" in value:
        out["sourceCodeUrl"] = value["source_code_url"]
    if "template_body" in value:
        out["templateBody"] = value["template_body"]
    if "template_url" in value:
        out["templateUrl"] = value["template_url"]
    return out


def deserialize_json(data: dict) -> CreateApplicationVersionRequest:
    out: CreateApplicationVersionRequest = {}  # type: ignore[typeddict-item]
    if "sourceCodeArchiveUrl" in data:
        out["source_code_archive_url"] = data["sourceCodeArchiveUrl"]
    if "sourceCodeUrl" in data:
        out["source_code_url"] = data["sourceCodeUrl"]
    if "templateBody" in data:
        out["template_body"] = data["templateBody"]
    if "templateUrl" in data:
        out["template_url"] = data["templateUrl"]
    return out

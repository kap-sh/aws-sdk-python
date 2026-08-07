"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ApplicationResourceLifecycleConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_version_lifecycle_config
    import capo_elastic_beanstalk.types.string


class ApplicationResourceLifecycleConfig(TypedDict, closed=True):
    service_role: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The ARN of an IAM service role that Elastic Beanstalk has permission to assume.</p> <p>The <code>ServiceRole</code> property is required the first time that you provide a <code>VersionLifecycleConfig</code> for the application in one of the supporting calls (<code>CreateApplication</code> or <code>UpdateApplicationResourceLifecycle</code>). After you provide it once, in either one of the calls, Elastic Beanstalk persists the Service Role with the application, and you don't need to specify it again in subsequent <code>UpdateApplicationResourceLifecycle</code> calls. You can, however, specify it in subsequent calls to change the Service Role to another value.</p>"""
    version_lifecycle_config: NotRequired[
        "capo_elastic_beanstalk.types.application_version_lifecycle_config.ApplicationVersionLifecycleConfig"
    ]
    """<p>Defines lifecycle settings for application versions.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ApplicationResourceLifecycleConfig, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "service_role" in value:
        pairs.append((f"{key_prefix}ServiceRole", str(value["service_role"])))
    if "version_lifecycle_config" in value:
        import capo_elastic_beanstalk.types.application_version_lifecycle_config

        capo_elastic_beanstalk.types.application_version_lifecycle_config.serialize_query(
            value["version_lifecycle_config"],
            pairs,
            f"{key_prefix}VersionLifecycleConfig",
        )


def deserialize_query(el: Element) -> ApplicationResourceLifecycleConfig:
    out: ApplicationResourceLifecycleConfig = {}  # type: ignore[typeddict-item]
    child_service_role = el.find("ServiceRole")
    if child_service_role is not None:
        out["service_role"] = str(child_service_role.text or "")
    child_version_lifecycle_config = el.find("VersionLifecycleConfig")
    if child_version_lifecycle_config is not None:
        import capo_elastic_beanstalk.types.application_version_lifecycle_config

        out["version_lifecycle_config"] = (
            capo_elastic_beanstalk.types.application_version_lifecycle_config.deserialize_query(
                child_version_lifecycle_config
            )
        )
    return out

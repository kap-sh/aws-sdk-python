"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#LicenseConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.instance_type
    import aws_sdk_compute_optimizer.types.license_edition
    import aws_sdk_compute_optimizer.types.license_model
    import aws_sdk_compute_optimizer.types.license_name
    import aws_sdk_compute_optimizer.types.license_version
    import aws_sdk_compute_optimizer.types.metrics_source
    import aws_sdk_compute_optimizer.types.number_of_cores
    import aws_sdk_compute_optimizer.types.operating_system


class LicenseConfiguration(TypedDict):
    number_of_cores: "aws_sdk_compute_optimizer.types.number_of_cores.NumberOfCores"
    """<p> The current number of cores associated with the instance. </p>"""
    instance_type: NotRequired[
        "aws_sdk_compute_optimizer.types.instance_type.InstanceType"
    ]
    """<p> The instance type used in the license. </p>"""
    operating_system: NotRequired[
        "aws_sdk_compute_optimizer.types.operating_system.OperatingSystem"
    ]
    """<p> The operating system of the instance. </p>"""
    license_edition: NotRequired[
        "aws_sdk_compute_optimizer.types.license_edition.LicenseEdition"
    ]
    """<p> The edition of the license for the application that runs on the instance. </p>"""
    license_name: NotRequired[
        "aws_sdk_compute_optimizer.types.license_name.LicenseName"
    ]
    """<p> The name of the license for the application that runs on the instance. </p>"""
    license_model: NotRequired[
        "aws_sdk_compute_optimizer.types.license_model.LicenseModel"
    ]
    """<p> The license type associated with the instance. </p>"""
    license_version: NotRequired[
        "aws_sdk_compute_optimizer.types.license_version.LicenseVersion"
    ]
    """<p> The version of the license for the application that runs on the instance. </p>"""
    metrics_source: NotRequired[
        "aws_sdk_compute_optimizer.types.metrics_source.MetricsSource"
    ]
    """<p> The list of metric sources required to generate recommendations for commercial software licenses. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseConfiguration) -> dict:
    out: dict = {}
    out["numberOfCores"] = value.get("number_of_cores", 0)
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "operating_system" in value:
        out["operatingSystem"] = value["operating_system"]
    if "license_edition" in value:
        import aws_sdk_compute_optimizer.types.license_edition

        out["licenseEdition"] = (
            aws_sdk_compute_optimizer.types.license_edition.serialize_aws_json_1_0(
                value["license_edition"]
            )
        )
    if "license_name" in value:
        import aws_sdk_compute_optimizer.types.license_name

        out["licenseName"] = (
            aws_sdk_compute_optimizer.types.license_name.serialize_aws_json_1_0(
                value["license_name"]
            )
        )
    if "license_model" in value:
        import aws_sdk_compute_optimizer.types.license_model

        out["licenseModel"] = (
            aws_sdk_compute_optimizer.types.license_model.serialize_aws_json_1_0(
                value["license_model"]
            )
        )
    if "license_version" in value:
        out["licenseVersion"] = value["license_version"]
    if "metrics_source" in value:
        import aws_sdk_compute_optimizer.types.metrics_source

        out["metricsSource"] = (
            aws_sdk_compute_optimizer.types.metrics_source.serialize_aws_json_1_0(
                value["metrics_source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseConfiguration:
    out: LicenseConfiguration = {}  # type: ignore[typeddict-item]
    if "numberOfCores" in data:
        out["number_of_cores"] = data["numberOfCores"]
    else:
        out["number_of_cores"] = 0
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "operatingSystem" in data:
        out["operating_system"] = data["operatingSystem"]
    if "licenseEdition" in data:
        import aws_sdk_compute_optimizer.types.license_edition

        out["license_edition"] = (
            aws_sdk_compute_optimizer.types.license_edition.deserialize_aws_json_1_0(
                data["licenseEdition"]
            )
        )
    if "licenseName" in data:
        import aws_sdk_compute_optimizer.types.license_name

        out["license_name"] = (
            aws_sdk_compute_optimizer.types.license_name.deserialize_aws_json_1_0(
                data["licenseName"]
            )
        )
    if "licenseModel" in data:
        import aws_sdk_compute_optimizer.types.license_model

        out["license_model"] = (
            aws_sdk_compute_optimizer.types.license_model.deserialize_aws_json_1_0(
                data["licenseModel"]
            )
        )
    if "licenseVersion" in data:
        out["license_version"] = data["licenseVersion"]
    if "metricsSource" in data:
        import aws_sdk_compute_optimizer.types.metrics_source

        out["metrics_source"] = (
            aws_sdk_compute_optimizer.types.metrics_source.deserialize_aws_json_1_0(
                data["metricsSource"]
            )
        )
    return out

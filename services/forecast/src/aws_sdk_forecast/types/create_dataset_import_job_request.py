"""Generated from Smithy shape ``com.amazonaws.forecast#CreateDatasetImportJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.data_source
    import aws_sdk_forecast.types.format
    import aws_sdk_forecast.types.geolocation_format
    import aws_sdk_forecast.types.import_mode
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.tags
    import aws_sdk_forecast.types.time_zone
    import aws_sdk_forecast.types.timestamp_format
    import aws_sdk_forecast.types.use_geolocation_for_time_zone


class CreateDatasetImportJobRequest(TypedDict):
    dataset_import_job_name: "aws_sdk_forecast.types.name.Name"
    """<p>The name for the dataset import job. We recommend including the current timestamp in the name, for example, <code>20190721DatasetImport</code>. This can help you avoid getting a <code>ResourceAlreadyExistsException</code> exception.</p>"""
    dataset_arn: "aws_sdk_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Forecast dataset that you want to import data to.</p>"""
    data_source: "aws_sdk_forecast.types.data_source.DataSource"
    """<p>The location of the training data to import and an Identity and Access Management (IAM) role that Amazon Forecast can assume to access the data. The training data must be stored in an Amazon S3 bucket.</p> <p>If encryption is used, <code>DataSource</code> must include an Key Management Service (KMS) key and the IAM role must allow Amazon Forecast permission to access the key. The KMS key and IAM role must match those specified in the <code>EncryptionConfig</code> parameter of the <a href=\"https://docs.aws.amazon.com/forecast/latest/dg/API_CreateDataset.html\">CreateDataset</a> operation.</p>"""
    timestamp_format: NotRequired[
        "aws_sdk_forecast.types.timestamp_format.TimestampFormat"
    ]
    """<p>The format of timestamps in the dataset. The format that you specify depends on the <code>DataFrequency</code> specified when the dataset was created. The following formats are supported</p> <ul> <li> <p>\"yyyy-MM-dd\"</p> <p>For the following data frequencies: Y, M, W, and D</p> </li> <li> <p>\"yyyy-MM-dd HH:mm:ss\"</p> <p>For the following data frequencies: H, 30min, 15min, and 1min; and optionally, for: Y, M, W, and D</p> </li> </ul> <p>If the format isn't specified, Amazon Forecast expects the format to be \"yyyy-MM-dd HH:mm:ss\".</p>"""
    time_zone: NotRequired["aws_sdk_forecast.types.time_zone.TimeZone"]
    """<p>A single time zone for every item in your dataset. This option is ideal for datasets with all timestamps within a single time zone, or if all timestamps are normalized to a single time zone. </p> <p>Refer to the <a href=\"http://joda-time.sourceforge.net/timezones.html\">Joda-Time API</a> for a complete list of valid time zone names.</p>"""
    use_geolocation_for_time_zone: (
        "aws_sdk_forecast.types.use_geolocation_for_time_zone.UseGeolocationForTimeZone"
    )
    """<p>Automatically derive time zone information from the geolocation attribute. This option is ideal for datasets that contain timestamps in multiple time zones and those timestamps are expressed in local time.</p>"""
    geolocation_format: NotRequired[
        "aws_sdk_forecast.types.geolocation_format.GeolocationFormat"
    ]
    """<p>The format of the geolocation attribute. The geolocation attribute can be formatted in one of two ways:</p> <ul> <li> <p> <code>LAT_LONG</code> - the latitude and longitude in decimal format (Example: 47.61_-122.33).</p> </li> <li> <p> <code>CC_POSTALCODE</code> (US Only) - the country code (US), followed by the 5-digit ZIP code (Example: US_98121).</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_forecast.types.tags.Tags"]
    """<p>The optional metadata that you apply to the dataset import job to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use <code>aws:</code>, <code>AWS:</code>, or any upper or lowercase combination of such as a prefix for keys as it is reserved for Amazon Web Services use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, then Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit.</p> </li> </ul>"""
    format: NotRequired["aws_sdk_forecast.types.format.Format"]
    """<p>The format of the imported data, CSV or PARQUET. The default value is CSV.</p>"""
    import_mode: NotRequired["aws_sdk_forecast.types.import_mode.ImportMode"]
    """<p>Specifies whether the dataset import job is a <code>FULL</code> or <code>INCREMENTAL</code> import. A <code>FULL</code> dataset import replaces all of the existing data with the newly imported data. An <code>INCREMENTAL</code> import appends the imported data to the existing data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetImportJobRequest) -> dict:
    out: dict = {}
    out["DatasetImportJobName"] = value["dataset_import_job_name"]
    out["DatasetArn"] = value["dataset_arn"]
    import aws_sdk_forecast.types.data_source

    out["DataSource"] = aws_sdk_forecast.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    if "timestamp_format" in value:
        out["TimestampFormat"] = value["timestamp_format"]
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    out["UseGeolocationForTimeZone"] = value.get("use_geolocation_for_time_zone", False)
    if "geolocation_format" in value:
        out["GeolocationFormat"] = value["geolocation_format"]
    if "tags" in value:
        import aws_sdk_forecast.types.tags

        out["Tags"] = aws_sdk_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    if "format" in value:
        out["Format"] = value["format"]
    if "import_mode" in value:
        import aws_sdk_forecast.types.import_mode

        out["ImportMode"] = aws_sdk_forecast.types.import_mode.serialize_aws_json_1_1(
            value["import_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetImportJobRequest:
    out: CreateDatasetImportJobRequest = {}  # type: ignore[typeddict-item]
    if "DatasetImportJobName" in data:
        out["dataset_import_job_name"] = data["DatasetImportJobName"]
    else:
        raise DeserializationError(
            "CreateDatasetImportJobRequest.dataset_import_job_name required"
        )
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    else:
        raise DeserializationError("CreateDatasetImportJobRequest.dataset_arn required")
    if "DataSource" in data:
        import aws_sdk_forecast.types.data_source

        out["data_source"] = (
            aws_sdk_forecast.types.data_source.deserialize_aws_json_1_1(
                data["DataSource"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetImportJobRequest.data_source required")
    if "TimestampFormat" in data:
        out["timestamp_format"] = data["TimestampFormat"]
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    if "UseGeolocationForTimeZone" in data:
        out["use_geolocation_for_time_zone"] = data["UseGeolocationForTimeZone"]
    else:
        out["use_geolocation_for_time_zone"] = False
    if "GeolocationFormat" in data:
        out["geolocation_format"] = data["GeolocationFormat"]
    if "Tags" in data:
        import aws_sdk_forecast.types.tags

        out["tags"] = aws_sdk_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "Format" in data:
        out["format"] = data["Format"]
    if "ImportMode" in data:
        import aws_sdk_forecast.types.import_mode

        out["import_mode"] = (
            aws_sdk_forecast.types.import_mode.deserialize_aws_json_1_1(
                data["ImportMode"]
            )
        )
    return out
